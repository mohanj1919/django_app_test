import React, { Component } from 'react'
import { Button, InputGroup } from 'react-bootstrap'
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table'
import './style.scss'
import 'react-bootstrap-table/dist/react-bootstrap-table-all.min.css'

export class CuratorProjects extends Component {
  render () {
    var customSearchField = () => {
      return (
        <InputGroup className='search-projects table-search-box'>
          <input type='text' placeholder='Search Projects' onChange={(e) => this.props.SearchProject(e)} className='form-control' />
          <InputGroup.Addon><i className='fa fa-search' /></InputGroup.Addon>
        </InputGroup>
      )
    }
    var tableCell = (cell, row) => {
      return (
        <span className='ques-data' title={cell}>{cell}</span>
      )
    }

    var options = {
      onPageChange: this.props.PageChanged,
      page: this.props.page,
      paginationShowsTotal: true,
      searchField: customSearchField,
      sizePerPageList: [{
        text: '10', value: 10
      }, {
        text: '20', value: 20
      }, {
        text: '50', value: 50
      }],
      onSortChange: this.props.SortChange
    }

    var activeFormatter = (cell, row) => {
      let url = `/chartreview/${row.project_id}/${row.id}`
      return (
        <div>
          <span>
            <span className='view-button'>
              <Button bsStyle='primary' disabled={!row.has_pending_patients} onClick={() => this.props.router.push(url)}
                title={!row.has_pending_patients ? 'No Patients available for curation in this cohort' : 'View Chart Review'}>
                <i className='fa fa-eye' aria-hidden='true' />
              </Button>
            </span>
          </span>
        </div>
      )
    }

    return (
      <div>
        <div className='projects-container'>
          <BootstrapTable
            data={this.props.projectsData ? this.props.projectsData : []}
            pagination
            striped
            hover
            fetchInfo={{
              dataTotalSize: this.props.totalCount
            }}
            search
            options={options}
            remote>
            <TableHeaderColumn dataFormat={tableCell} dataField='project_name' isKey>Project Name</TableHeaderColumn>
            <TableHeaderColumn dataFormat={tableCell} dataField='name' >Cohort Name</TableHeaderColumn>
            <TableHeaderColumn dataFormat={tableCell} dataField='completedPatients' >Completed Patients</TableHeaderColumn>
            <TableHeaderColumn dataFormat={tableCell} dataField='totalPatients' >Total Patients</TableHeaderColumn>
            <TableHeaderColumn dataFormat={activeFormatter}>Actions</TableHeaderColumn>
          </BootstrapTable>
        </div>
      </div>
    )
  }
}

export default CuratorProjects
