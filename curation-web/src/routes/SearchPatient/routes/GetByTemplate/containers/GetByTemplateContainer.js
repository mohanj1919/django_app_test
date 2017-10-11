import { connect } from 'react-redux'
import GetByTemplate from '../components/GetByTemplate'
import { dispatchToProps } from '../modules/getbytemplate'

const mapStateToProps = (state) => ({
  ...state.getbytemplate
})

const mapDispatchToProps = {
  ...dispatchToProps()
}

export default connect(mapStateToProps, mapDispatchToProps)(GetByTemplate)
