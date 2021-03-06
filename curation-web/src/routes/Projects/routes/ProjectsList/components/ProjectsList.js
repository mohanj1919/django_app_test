import React, { Component } from 'react'
import './style.scss'
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table'
import { Button, InputGroup } from 'react-bootstrap'
import 'react-bootstrap-table/dist/react-bootstrap-table-all.min.css'

class ProjectsList extends Component {
  componentDidMount () {
    this
      .props
      .fetchCohorts()
  }

  render () {
    var activeFormatter = (cell, row) => {
      return (
        <div>
          <Button bsStyle='primary' onClick={() => this.props.EditCohortsList(row.id)} title={'Edit Project'}>
            <i className='fa fa-pencil-square-o' aria-hidden='true' />
          </Button>
        </div>
      )
    }

    var tableCell = (cell, row) => {
      return (
        <span className='user-data' title={cell}>{cell}</span>
      )
    }

    var createCustomButtonGroup = () => {
      return (
        <Button
          bsStyle='primary'
          onClick={() => {
            this
            .props
            .router
            .push('/projects/configure')
          }}>
          <i className='fa fa-plus' aria-hidden='true' /> Add Project
        </Button>
      )
    }
    var customSearchField = (props) => {
      return (
        <InputGroup className='input-group table-search-field pull-right table-search-box'>
          <input type='text' placeholder='Search Projects' onKeyUp={this.props.SearchCohort} className='form-control' />
          <InputGroup.Addon><i className='fa fa-search' /></InputGroup.Addon>
        </InputGroup>
      )
    }
    var options = {
      paginationShowsTotal: true,
      onPageChange: this.props.PageChange,
      searchField: () => customSearchField(),
      btnGroup: createCustomButtonGroup,
      page: this.props.pageNumber,
      sizePerPageList: [
        {
          text: '10',
          value: 10
        }, {
          text: '25',
          value: 25
        }, {
          text: '50',
          value: 50
        }
      ],
      onSortChange: this.props.SortChange
    }

    return (
      <div className='container'>
        <BootstrapTable
          data={this.props.cohorts}
          striped
          hover
          search
          className={'cohorts-table bootstrap-custom-table'}
          options={options}
          fetchInfo={{
            dataTotalSize: this.props.totalCount
          }}
          pagination
          remote>
          <TableHeaderColumn
            dataFormat={tableCell}
            dataField='name'
            isKey
            dataSort>Name</TableHeaderColumn>
          <TableHeaderColumn dataFormat={tableCell} dataField='description'>Description</TableHeaderColumn>
          <TableHeaderColumn dataFormat={tableCell} dataField='total'>Total</TableHeaderColumn>
          <TableHeaderColumn dataFormat={tableCell} dataField='completed'>Completed</TableHeaderColumn>
          <TableHeaderColumn
            dataFormat={tableCell}
            dataField='inProgress'>In-Progress</TableHeaderColumn>
          <TableHeaderColumn dataFormat={tableCell} dataField='remaining'>Remaining</TableHeaderColumn>
          <TableHeaderColumn dataFormat={activeFormatter}>Actions</TableHeaderColumn>
        </BootstrapTable>
      </div>
    )
  }
}
export default ProjectsList
