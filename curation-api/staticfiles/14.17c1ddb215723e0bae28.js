webpackJsonp([14],{

/***/ 1228:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


exports.__esModule = true;

var _from = __webpack_require__(329);

var _from2 = _interopRequireDefault(_from);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = function (arr) {
  if (Array.isArray(arr)) {
    for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) {
      arr2[i] = arr[i];
    }

    return arr2;
  } else {
    return (0, _from2.default)(arr);
  }
};

/***/ }),

/***/ 1293:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_classCallCheck__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_classCallCheck___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_classCallCheck__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_createClass__ = __webpack_require__(42);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_createClass___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_createClass__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_babel_runtime_helpers_possibleConstructorReturn__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_babel_runtime_helpers_possibleConstructorReturn___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2_babel_runtime_helpers_possibleConstructorReturn__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_babel_runtime_helpers_inherits__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_babel_runtime_helpers_inherits___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3_babel_runtime_helpers_inherits__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_react__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5_react_bootstrap__ = __webpack_require__(105);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__AdminSettingsStyles_scss__ = __webpack_require__(1349);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__AdminSettingsStyles_scss___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_6__AdminSettingsStyles_scss__);








var AdminSettings = function (_Component) {
  __WEBPACK_IMPORTED_MODULE_3_babel_runtime_helpers_inherits___default()(AdminSettings, _Component);

  function AdminSettings() {
    __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_classCallCheck___default()(this, AdminSettings);

    return __WEBPACK_IMPORTED_MODULE_2_babel_runtime_helpers_possibleConstructorReturn___default()(this, (AdminSettings.__proto__ || Object.getPrototypeOf(AdminSettings)).apply(this, arguments));
  }

  __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_createClass___default()(AdminSettings, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      this.props.GetAdminSettings();
    }
  }, {
    key: 'render',
    value: function render() {
      var _this2 = this;

      return __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
        'div',
        { className: 'settings-data-div' },
        this.props.SettingsData && this.props.SettingsData.length > 0 ? __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
          'div',
          { className: 'container' },
          __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
            'div',
            { className: 'col-md-6' },
            this.props.groups ? this.props.groups.map(function (grp, i) {
              return __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                'div',
                { key: i },
                ' ',
                grp ? __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                  'label',
                  null,
                  grp
                ) : null,
                __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                  'div',
                  { className: 'well' },
                  _this2.props.SettingsData.map(function (sg, j) {
                    return sg.settings_group === grp ? __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                      __WEBPACK_IMPORTED_MODULE_5_react_bootstrap__["c" /* FormGroup */],
                      { className: 'individual-setting', validationState: sg.ValidationState, key: j },
                      __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                        'div',
                        null,
                        __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                          __WEBPACK_IMPORTED_MODULE_5_react_bootstrap__["e" /* ControlLabel */],
                          { className: 'required' },
                          sg.text
                        )
                      ),
                      __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                        'div',
                        null,
                        __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_5_react_bootstrap__["f" /* FormControl */], { type: sg.type ? sg.type : 'text', name: sg.setting,
                          value: sg.value, onChange: _this2.props.HandleTextEdit }),
                        sg.Help ? __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                          __WEBPACK_IMPORTED_MODULE_5_react_bootstrap__["d" /* HelpBlock */],
                          null,
                          sg.Help
                        ) : null
                      )
                    ) : null;
                  })
                )
              );
            }) : null,
            __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
              'div',
              { className: 'btn-set' },
              __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                'span',
                null,
                __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                  'span',
                  { className: 'save-btn' },
                  __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                    __WEBPACK_IMPORTED_MODULE_5_react_bootstrap__["b" /* Button */],
                    { bsStyle: 'success', onClick: function onClick() {
                        _this2.props.SubmitSettings();
                      } },
                    'Save'
                  )
                ),
                __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                  'span',
                  { className: 'cancel-btn' },
                  __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
                    __WEBPACK_IMPORTED_MODULE_5_react_bootstrap__["b" /* Button */],
                    { bsStyle: 'default', onClick: function onClick() {
                        _this2.props.CancelEditing();
                      } },
                    'Cancel'
                  )
                )
              )
            )
          )
        ) : __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
          'div',
          { className: 'no-settings-info' },
          __WEBPACK_IMPORTED_MODULE_4_react___default.a.createElement(
            'h4',
            null,
            'No settings found'
          )
        )
      );
    }
  }]);

  return AdminSettings;
}(__WEBPACK_IMPORTED_MODULE_4_react__["Component"]);

/* harmony default export */ __webpack_exports__["a"] = (AdminSettings);

/***/ }),

/***/ 1349:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 738:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (immutable) */ __webpack_exports__["GetAdminSettings"] = GetAdminSettings;
/* harmony export (immutable) */ __webpack_exports__["HandleTextEdit"] = HandleTextEdit;
/* harmony export (immutable) */ __webpack_exports__["SubmitSettings"] = SubmitSettings;
/* harmony export (immutable) */ __webpack_exports__["CancelEditing"] = CancelEditing;
/* harmony export (immutable) */ __webpack_exports__["default"] = chartReviewReducer;
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_defineProperty__ = __webpack_require__(303);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_defineProperty___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_defineProperty__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_toConsumableArray__ = __webpack_require__(1228);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_toConsumableArray___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_toConsumableArray__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__lib_axios__ = __webpack_require__(305);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__config__ = __webpack_require__(177);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__modules_global_js__ = __webpack_require__(176);



var _ACTION_HANDLERS;






var SET_PROP = 'SET_PROP';
var SETTINGS_DATA = 'SETTINGS_DATA';
var VALIDATE_SETTINGS = 'VALIDATE_SETTINGS';
var SET_SERVER_VALIDATION = 'SET_SERVER_VALIDATION';

// action creators
function GetAdminSettings() {
  return function (dispatch) {
    var groupedData = [];
    var groups = [];
    dispatch({ type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["g" /* TOGGLE_LOADING */], payload: true });
    __WEBPACK_IMPORTED_MODULE_2__lib_axios__["a" /* default */].get(__WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].api.get_admin_settings).then(function (response) {
      if (response && response.data) {
        groupedData = response.data.results;
        groups = [].concat(__WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_toConsumableArray___default()(new Set(response.data.results.map(function (item) {
          return item.settings_group;
        }))));
      }
      dispatch({
        type: SETTINGS_DATA,
        payload: groupedData,
        groups: groups
      });
      dispatch({ type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["g" /* TOGGLE_LOADING */], payload: false });
    }).catch(function (errors) {
      dispatch({
        type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["i" /* TOGGLE_NOTIFICATION */],
        showBanner: true,
        showTime: 3000,
        showType: 'error',
        showMessage: 'Error in fetching Settings'
      });
      dispatch({ type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["g" /* TOGGLE_LOADING */], payload: false });
    });
  };
}
function HandleTextEdit(event) {
  return function (dispatch) {
    dispatch({
      type: SET_PROP,
      payload: {
        key: event.target.name,
        value: event.target.value
      }
    });
  };
}
function SubmitSettings() {
  return function (dispatch, getState) {
    dispatch({
      type: VALIDATE_SETTINGS
    });
    if (getState().adminsettings.isValid) {
      __WEBPACK_IMPORTED_MODULE_2__lib_axios__["a" /* default */].post(__WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].api.get_admin_settings, getState().adminsettings.SettingsData).then(function (response) {
        dispatch({
          type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["i" /* TOGGLE_NOTIFICATION */],
          showBanner: true,
          showTime: 3000,
          showType: 'success',
          showMessage: 'Settings Successfully updated'
        });
        dispatch(GetAdminSettings());
      }).catch(function (errors) {
        if (errors && errors.response && errors.response.data && errors.response.data.errors) {
          dispatch({
            type: SET_SERVER_VALIDATION,
            payload: errors && errors.response && errors.response.data && errors.response.data.errors ? errors.response.data.errors : null
          });
        } else {
          dispatch({
            type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["i" /* TOGGLE_NOTIFICATION */],
            showBanner: true,
            showTime: 3000,
            showType: 'error',
            showMessage: 'Unable to Update Settings'
          });
        }
      });
    }
  };
}
function CancelEditing() {
  return function (dispatch) {
    dispatch({
      type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["i" /* TOGGLE_NOTIFICATION */],
      payload: true,
      showTime: null,
      showType: 'warning',
      showMessage: 'Are you sure want to cancel changes ?',
      messageTitle: 'Cancel Changes',
      successCb: function successCb() {
        dispatch(GetAdminSettings());
        dispatch({
          type: __WEBPACK_IMPORTED_MODULE_4__modules_global_js__["j" /* HIDE_BANNER */]
        });
      }
    });
  };
}
// action handlers
var ACTION_HANDLERS = (_ACTION_HANDLERS = {}, __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_defineProperty___default()(_ACTION_HANDLERS, SET_PROP, function (state, action) {
  var settingsObj = [];
  if (action.payload && state.SettingsData) {
    state.SettingsData.map(function (sd, i) {
      if (sd.setting == action.payload.key) {
        sd.ValidationState = null;
        sd.Help = null;
        sd.value = action.payload.value;
      }
      settingsObj.push(sd);
    });
  }
  return Object.assign({}, state, {
    SettingsData: settingsObj
  });
}), __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_defineProperty___default()(_ACTION_HANDLERS, SETTINGS_DATA, function (state, action) {
  return Object.assign({}, state, { SettingsData: action.payload, groups: action.groups });
}), __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_defineProperty___default()(_ACTION_HANDLERS, VALIDATE_SETTINGS, function (state, action) {
  var valid = true;
  if (state.SettingsData) {
    state.SettingsData.map(function (sd, i) {
      if (!sd.value) {
        valid = false;
        sd.ValidationState = 'error';
      }
    });
  }
  return Object.assign({}, state, { isValid: valid });
}), __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_defineProperty___default()(_ACTION_HANDLERS, SET_SERVER_VALIDATION, function (state, action) {
  var settingsData = [];
  if (state.SettingsData) {
    state.SettingsData.map(function (sd, i) {
      if (action.payload && Object.keys(action.payload).indexOf(sd.setting) > -1) {
        sd.ValidationState = 'error';
        sd.Help = action.payload[sd.setting] && action.payload[sd.setting].length > 0 ? action.payload[sd.setting][0].charAt(0).toUpperCase() + action.payload[sd.setting][0].slice(1) : null;
      }
      settingsData.push(sd);
    });
  }
  return Object.assign({}, state, { SettingsData: settingsData });
}), _ACTION_HANDLERS);

// reducer
var initialState = {};
function chartReviewReducer() {
  var state = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : initialState;
  var action = arguments[1];

  var handler = ACTION_HANDLERS[action.type];
  return handler ? handler(state, action) : state;
}

/***/ }),

/***/ 753:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react_redux__ = __webpack_require__(172);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__components_AdminSettings_js__ = __webpack_require__(1293);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__modules_adminSettings_js__ = __webpack_require__(738);




var mapStateToProps = function mapStateToProps(state) {
  return Object.assign({}, state.adminsettings);
};

var mapDispatchToProps = {
  GetAdminSettings: __WEBPACK_IMPORTED_MODULE_2__modules_adminSettings_js__["GetAdminSettings"],
  HandleTextEdit: __WEBPACK_IMPORTED_MODULE_2__modules_adminSettings_js__["HandleTextEdit"],
  SubmitSettings: __WEBPACK_IMPORTED_MODULE_2__modules_adminSettings_js__["SubmitSettings"],
  CancelEditing: __WEBPACK_IMPORTED_MODULE_2__modules_adminSettings_js__["CancelEditing"]
};

/* harmony default export */ __webpack_exports__["default"] = (__webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0_react_redux__["b" /* connect */])(mapStateToProps, mapDispatchToProps)(__WEBPACK_IMPORTED_MODULE_1__components_AdminSettings_js__["a" /* default */]));

/***/ })

});
//# sourceMappingURL=14.17c1ddb215723e0bae28.js.map