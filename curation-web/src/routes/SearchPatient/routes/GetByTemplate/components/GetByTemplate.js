import React, { Component } from 'react'
import { DropdownButton, MenuItem, InputGroup } from 'react-bootstrap'
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table'
import './Styles.scss'

class ShowPatients extends Component {
  componentDidMount () {
    this.props.GetCompletedTemplates()
  }
  render () {
    var projectCell = (cell, row) => {
      return (
        <span className='patient-search-data' title={cell.name}>{cell.name}</span>
      )
    }
    var activeFormatter = (cell, row) => {
      return (
        <div>
          <span className='download-att'>
            <DropdownButton className='fa fa-download'>
              <MenuItem eventKey='1' onClick={() => this.props.ExtractCRFs(row, 'csv')}>CSV</MenuItem>
              <MenuItem eventKey='1' onClick={() => this.props.ExtractCRFs(row, 'JSON')}>JSON</MenuItem>
            </DropdownButton>
          </span>
        </div>
      )
    }
    var customSearchField = (props) => {
      return (
        <InputGroup className='input-group table-search-field pull-right table-search-box'>
          <input type='text' placeholder='Search' onKeyUp={this.props.SearchTemplates} className='form-control' />
          <InputGroup.Addon><i className='fa fa-search' /></InputGroup.Addon>
        </InputGroup>
      )
    }
    var options = {
      onPageChange: this.props.PageChange,
      page: this.props.pageNumber,
      paginationShowsTotal: true,
      searchField: customSearchField,
      sizePerPageList: [{
        text: '10', value: 10
      },
      {
        text: '25', value: 25
      },
      {
        text: '50', value: 50
      }],
      onSortChange: this.props.SortChange
    }
    return (
      <div className='container'>
        <div className='row'>
          <div className='col-md-12'>
            <BootstrapTable
              data={this.props.patients}
              striped
              search
              hover
              className={'patients-search-table'}
              fetchInfo={{
                dataTotalSize: this.props.totalCount
              }}
              options={options}
              pagination
              remote>
              <TableHeaderColumn dataFormat={projectCell} isKey dataField='project' dataSort>Project</TableHeaderColumn>
              <TableHeaderColumn dataFormat={projectCell} dataField='cohort' dataSort>Cohort</TableHeaderColumn>
              <TableHeaderColumn dataFormat={projectCell} dataField='crf_template' dataSort>CRF Template</TableHeaderColumn>
              <TableHeaderColumn dataFormat={activeFormatter} columnClassName='patients-actions'>Actions</TableHeaderColumn>
            </BootstrapTable>
          </div>
        </div>
      </div>
    )
  }
}

export default ShowPatients
