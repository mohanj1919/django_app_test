import React, { PropTypes } from 'react'
import 'react-bootstrap-table/dist/react-bootstrap-table-all.min.css'
import './Styles.scss'

function SearchPatients ({ children }) {
  return (
    <div>
      <br />
      {children}
    </div>
  )
}

SearchPatients.propTypes = {
  children: PropTypes.element
}

export default SearchPatients
