webpackJsonp([14],{1209:function(e,t,n){"use strict";t.__esModule=!0;var a=n(324),s=function(e){return e&&e.__esModule?e:{default:e}}(a);t.default=function(e){if(Array.isArray(e)){for(var t=0,n=Array(e.length);t<e.length;t++)n[t]=e[t];return n}return(0,s.default)(e)}},1274:function(e,t,n){"use strict";var a=n(1),s=n.n(a),i=n(40),r=n.n(i),l=n(3),o=n.n(l),u=n(2),c=n.n(u),p=n(0),d=n.n(p),g=n(104),m=n(1330),f=(n.n(m),function(e){function t(){return s()(this,t),o()(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return c()(t,e),r()(t,[{key:"componentDidMount",value:function(){this.props.GetAdminSettings()}},{key:"render",value:function(){var e=this;return d.a.createElement("div",{className:"settings-data-div"},this.props.SettingsData&&this.props.SettingsData.length>0?d.a.createElement("div",{className:"container"},d.a.createElement("div",{className:"col-md-6"},this.props.groups?this.props.groups.map(function(t,n){return d.a.createElement("div",{key:n}," ",t?d.a.createElement("label",null,t):null,d.a.createElement("div",{className:"well"},e.props.SettingsData.map(function(n,a){return n.settings_group===t?d.a.createElement(g.c,{className:"individual-setting",validationState:n.ValidationState,key:a},d.a.createElement("div",null,d.a.createElement(g.e,{className:"required"},n.text)),d.a.createElement("div",null,d.a.createElement(g.f,{type:n.type?n.type:"text",name:n.setting,value:n.value,onChange:e.props.HandleTextEdit}),n.Help?d.a.createElement(g.d,null,n.Help):null)):null})))}):null,d.a.createElement("div",{className:"btn-set"},d.a.createElement("span",null,d.a.createElement("span",{className:"save-btn"},d.a.createElement(g.b,{bsStyle:"success",onClick:function(){e.props.SubmitSettings()}},"Save")),d.a.createElement("span",{className:"cancel-btn"},d.a.createElement(g.b,{bsStyle:"default",onClick:function(){e.props.CancelEditing()}},"Cancel")))))):d.a.createElement("div",{className:"no-settings-info"},d.a.createElement("h4",null,"No settings found")))}}]),t}(p.Component));t.a=f},1330:function(e,t){},726:function(e,t,n){"use strict";function a(){return function(e){var t=[],n=[];e({type:f.g,payload:!0}),g.a.get(m.a.api.get_admin_settings).then(function(a){a&&a.data&&(t=a.data.results,n=[].concat(d()(new Set(a.data.results.map(function(e){return e.settings_group}))))),e({type:S,payload:t,groups:n}),e({type:f.g,payload:!1})}).catch(function(t){e({type:f.i,showBanner:!0,showTime:3e3,showType:"error",showMessage:"Error in fetching Settings"}),e({type:f.g,payload:!1})})}}function s(e){return function(t){t({type:y,payload:{key:e.target.name,value:e.target.value}})}}function i(){return function(e,t){e({type:h}),t().adminsettings.isValid&&g.a.post(m.a.api.get_admin_settings,t().adminsettings.SettingsData).then(function(t){e({type:f.i,showBanner:!0,showTime:3e3,showType:"success",showMessage:"Settings Successfully updated"}),e(a())}).catch(function(t){e(t&&t.response&&t.response.data&&t.response.data.errors?{type:v,payload:t&&t.response&&t.response.data&&t.response.data.errors?t.response.data.errors:null}:{type:f.i,showBanner:!0,showTime:3e3,showType:"error",showMessage:"Unable to Update Settings"})})}}function r(){return function(e){e({type:f.i,payload:!0,showTime:null,showType:"warning",showMessage:"Are you sure want to cancel changes ?",messageTitle:"Cancel Changes",successCb:function(){e(a()),e({type:f.j})}})}}function l(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:b,t=arguments[1],n=E[t.type];return n?n(e,t):e}Object.defineProperty(t,"__esModule",{value:!0}),t.GetAdminSettings=a,t.HandleTextEdit=s,t.SubmitSettings=i,t.CancelEditing=r,t.default=l;var o,u=n(299),c=n.n(u),p=n(1209),d=n.n(p),g=n(301),m=n(175),f=n(174),y="SET_PROP",S="SETTINGS_DATA",h="VALIDATE_SETTINGS",v="SET_SERVER_VALIDATION",E=(o={},c()(o,y,function(e,t){var n=[];return t.payload&&e.SettingsData&&e.SettingsData.map(function(e,a){e.setting==t.payload.key&&(e.ValidationState=null,e.Help=null,e.value=t.payload.value),n.push(e)}),Object.assign({},e,{SettingsData:n})}),c()(o,S,function(e,t){return Object.assign({},e,{SettingsData:t.payload,groups:t.groups})}),c()(o,h,function(e,t){var n=!0;return e.SettingsData&&e.SettingsData.map(function(e,t){e.value||(n=!1,e.ValidationState="error")}),Object.assign({},e,{isValid:n})}),c()(o,v,function(e,t){var n=[];return e.SettingsData&&e.SettingsData.map(function(e,a){t.payload&&Object.keys(t.payload).indexOf(e.setting)>-1&&(e.ValidationState="error",e.Help=t.payload[e.setting]&&t.payload[e.setting].length>0?t.payload[e.setting][0].charAt(0).toUpperCase()+t.payload[e.setting][0].slice(1):null),n.push(e)}),Object.assign({},e,{SettingsData:n})}),o),b={}},741:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=n(80),s=n(1274),i=n(726),r=function(e){return Object.assign({},e.adminsettings)},l={GetAdminSettings:i.GetAdminSettings,HandleTextEdit:i.HandleTextEdit,SubmitSettings:i.SubmitSettings,CancelEditing:i.CancelEditing};t.default=n.i(a.connect)(r,l)(s.a)}});
//# sourceMappingURL=14.d4a58e7c0e445f9f0250.js.map