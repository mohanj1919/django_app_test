AWS_DEFAULT_REGION=us-east-1
APP=curation
PR=https://api.github.com/repos/$TRAVIS_REPO_SLUG/pulls/$TRAVIS_PULL_REQUEST
AWS_ACCOUNT=762653616445
DEVOPS_ENV=test
COMPOSE_IMAGE=curation
AWS_ACCESS_KEY_ID=AKIAIHAHB63K53UJDXAQ
AWS_DEFAULT_REGION=us-east-1
AWS_SECRET_ACCESS_KEY=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
DOCKER_AWS_ENV="-e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN -e AWS_SESSION_EXPIRATION=$AWS_SESSION_EXPIRATION"
DOCKER_AWS_ENV_DEPLOY_USER="-e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN -e AWS_SESSION_EXPIRATION=$AWS_SESSION_EXPIRATION"
REPO_PREFIX=boc-${DEVOPS_ENV}-
REV_DATE=$(date +%Y%m%d%H%M%S)
REV="${REV_DATE}-saiteja}"
ECR_REGISTRY_HOST=${AWS_ACCOUNT}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
ECR_REPO_NAME=${REPO_PREFIX}${APP}
ECS_IMAGE=${ECR_REGISTRY_HOST}/${ECR_REPO_NAME}
ECS_CLUSTER=boc-test-curation
ECS_SERVICE=${REPO_PREFIX}${APP}
ECS_TASK=${REPO_PREFIX}${APP}
CACHE_TAG=cache_$BRANCH
DOCKER_COMPOSE_VERSION=1.5.2

cat .env_dev >> .env
  
  # Build the UI app
docker-compose -f docker-compose-travis.yml build curation-web
set -e
docker-compose -f docker-compose-travis.yml up curation-web

  # Run tests with docker-compose
  #- docker-compose -f docker-compose-travis.yml up -d postgres
  #- |
  #  # fail fast
  #  set -e
  #  docker-compose -f docker-compose-travis.yml run app

  # Build with docker-compose
# docker-compose -f docker-compose-travis.yml build app


set -e
echo "Performing deploy for branch $BRANCH"
eval $(docker run ${DOCKER_AWS_ENV_DEPLOY_USER} betteroutcomes/aws-ecs-deploy aws-assume-role $AWS_ACCOUNT ops-deployer)
eval $(aws ecr get-login --no-include-email --region us-east-1)

# Tag docker-compose built image with ECR repo+tags and push them
docker tag $COMPOSE_IMAGE $ECS_IMAGE:latest && docker push $ECS_IMAGE:latest

# docker tag $COMPOSE_IMAGE $ECS_IMAGE:${REV} && docker push $ECS_IMAGE:${REV}

# The ID world and the DEID world handle their use of the schema repository differently.  In the DEID world
# schema is a task that migrates the stdstore.  In the ID world, schema is a service that provides an API.

# Update the ECS service
echo "${DOCKER_AWS_ENV}"

docker run ${DOCKER_AWS_ENV} betteroutcomes/aws-ecs-deploy aws-ecs-deploy ${ECS_CLUSTER} ${ECS_SERVICE} $ECS_IMAGE:latest

# Clean up old images
docker run ${DOCKER_AWS_ENV} betteroutcomes/aws-ecs-deploy aws-ecr-clean ${ECR_REPO_NAME} 40

# save cache of docker image to make subsequent runs faster
docker tag $COMPOSE_IMAGE $ECS_IMAGE:$CACHE_TAG && docker push $ECS_IMAGE:$CACHE_TAG
