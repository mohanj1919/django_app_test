import { injectReducer } from '../../../../store/reducers'

export default (store) => ({
  path: 'download_by_template',
  getComponent (nextState, cb) {
    require.ensure([], (require) => {
      const GetByTemplate = require('./containers/GetByTemplateContainer').default
      const reducer = require('./modules/getbytemplate').default

      /*  Add the reducer to the store on key 'managecasereportform'  */
      injectReducer(store, { key: 'getbytemplate', reducer })

      /*  Return getComponent   */
      cb(null, GetByTemplate)

      /* Webpack named bundle   */
    }, 'getbytemplate')
  }
})
