import {
  HIDE_BANNER,
  TOGGLE_NOTIFICATION,
  TOGGLE_LOADING,
  DownloadFile
} from '../../../../../modules/global.js'
import config from '../../../../../config'
import Papa from 'papaparse'
import axios from '../../../../../lib/axios'
import _ from 'lodash'

const SET_PROP = 'SET_PROP'

var handleEvent = (e) => {
  return (dispatch, getState) => {}
}

var GetCompletedTemplates = () => {
  return (dispatch, getState) => {
    dispatch(_getTemplates())
  }
}

var _getTemplates = (params) => {
  return (dispatch, getState) => {
    axios.get(config.api.get_completed_project_chart_reviews, {
      params: { ...params
      }
    }).then((response) => {
      dispatch({
        type: SET_PROP,
        payload: {
          key: 'totalCount',
          value: response.data.count
        }
      })
      dispatch({
        type: SET_PROP,
        payload: {
          key: 'patients',
          value: response.data.results
        }
      })
    }).catch((e) => {
      console.log(`ERROR: ${e}`)
    })
  }
}

var PageChange = (page, sizePerPage) => {
  return (dispatch, getState) => {
    let searchParams = getState().getbytemplate.searchParams || {}
    searchParams.page = page
    searchParams.page_size = sizePerPage
    dispatch({
      type: SET_PROP,
      payload: {
        key: 'searchParams',
        value: searchParams
      }
    })

    dispatch(_getTemplates(searchParams))
  }
}

var SortChange = (sortName, sortOrder) => {
  return (dispatch, getState) => {
    let searchParams = getState().getbytemplate.searchParams || {}
    searchParams.sortName = sortName
    searchParams.sortOrder = sortOrder
    dispatch({
      type: SET_PROP,
      payload: {
        key: 'searchParams',
        value: searchParams
      }
    })
    return dispatch(PageChange(getState().getbytemplate.pageNumber, getState().getbytemplate.pageSize))
  }
}

function SearchTemplates (searchText, colInfos, multiColumnSearch) {
  return (dispatch, getState) => {
    let searchParams = getState().getbytemplate.searchParams || {}
    searchParams.searchParam = searchText.target.value
    dispatch({
      type: SET_PROP,
      payload: {
        key: 'searchParams',
        value: searchParams
      }
    })
    return dispatch(PageChange(1, getState().getbytemplate.pageSize))
  }
}

var ExtractCRFs = (patientData, type) => {
  return (dispatch) => {
    let params = {
      project_id: patientData.project.id,
      cohort_id: patientData.cohort.id,
      crf_template_id: patientData.crf_template.id
    }
    dispatch({
      type: TOGGLE_LOADING,
      payload: true
    })
    axios.get('/clinical/chartreview/get_chart_review_response', {
      params: params
    }).then(function (response) {
      let data = {
        project_name: response.data[0].project.name,
        cohort_name: response.data[0].cohort.name,
        template_name: response.data[0].crf_templates[0].name
      }
      let fileName = `${data.project_name}_${data.cohort_name}_${data.template_name}`

      if (type === 'csv') {
        let questions = []
        _.map(response.data, (patient) => {
          _.map(patient.crf_templates, (item) => {
            _.map(item.questions, (question) => {
              data.patient_id = patient.patient.patient_id
              Object.assign(question, data)
            })
            questions.push.apply(questions, item.questions)
          })
        })
        DownloadFile(Papa.unparse(questions, {
          delimiter: '	'
        }), `${fileName}_excel.csv`)
      } else {
        data.crf_templates = response.data
        DownloadFile(JSON.stringify(data), `${fileName}_object.json`)
      }
    })
    dispatch({
      type: TOGGLE_LOADING,
      payload: false
    })
  }
}

const ACTION_HANDLERS = {
  [SET_PROP]: (state, action) => {
    return Object.assign({}, state, {
      [action.payload.key]: action.payload.value
    })
  }
}

const initialState = {
  pageNumber: 1,
  searchParams: {}
}

export default function getByTemplateReducer(state = initialState, action) {
  const handler = ACTION_HANDLERS[action.type]
  return handler ?
    handler(state, action) :
    state
}

export function dispatchToProps() {
  return {
    PageChange,
    handleEvent,
    SortChange,
    ExtractCRFs,
    GetCompletedTemplates,
    SearchTemplates
  }
}
