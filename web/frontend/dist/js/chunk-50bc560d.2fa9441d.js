(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-50bc560d"],{"078e":function(t,e,o){"use strict";o.r(e);var s=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("Layout",{staticStyle:{"min-height":"calc(100vh - 128px)",width:"80%",margin:"0 auto"}},[o("Header",{staticStyle:{background:"#f8f8f9",padding:"0"}},[o("Button",{attrs:{shape:"circle",size:"large",type:"primary"},on:{click:function(e){return t.$router.push("/center/workflow/create")}}},[t._v("\n      创建新工作流 ")]),t._v(" \n    "),o("Button",{attrs:{icon:"md-refresh",shape:"circle",size:"large",type:"default"},on:{click:function(e){t.refreshWorkflows(function(){return t.selectWorkflow(t.selected_idx)})}}})],1),o("Layout",{staticStyle:{height:"100%",background:"#fff",padding:"16px"}},[o("Row",{staticStyle:{height:"100%"}},[o("Col",{staticStyle:{height:"100%"},attrs:{xs:8,sm:8,md:6,lg:4}},[o("Layout",{staticStyle:{height:"100%","overflow-y":"auto",background:"#fff"}},[o("h2",[t._v("工作流列表")]),o("br"),o("ul",t._l(t.workflows,function(e,s){return o("li",{key:s,staticClass:"workflow-wrapper",attrs:{id:"workflow"+s},on:{click:function(e){return e.preventDefault(),e.stopPropagation(),t.selectWorkflow(s)}}},[o("div",{staticClass:"workflow-name"},[o("Badge",{attrs:{status:"default"}}),t._v("\n                "+t._s(e.name)+"\n              ")],1)])}),0)])],1),o("Col",{staticStyle:{height:"100%","padding-left":"16px"},attrs:{xs:16,sm:16,md:18,lg:20}},[t.current_workflow?o("Layout",[o("WorkflowView",{key:t.selected_idx,attrs:{workflowInfo:t.current_workflow}})],1):t._e()],1)],1)],1)],1)},n=[],r=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("Layout",{staticStyle:{background:"#fff",padding:"20px"}},[o("Row",[o("Menu",{attrs:{mode:"horizontal",theme:"light","active-name":"overview"},on:{"on-select":function(e){t.currentTab=e}}},[o("h2",{staticStyle:{display:"inline-block",float:"left","margin-right":"20px"}},[t._v("\n        "+t._s(t.workflowInfo.name)+"\n      ")]),o("MenuItem",{attrs:{name:"overview"}},[t._v("\n        概览\n      ")]),o("MenuItem",{attrs:{name:"edit"}},[t._v("\n        编辑\n      ")]),o("MenuItem",{attrs:{name:"test"}},[t._v("\n        测试\n      ")])],1)],1),o("Row",{directives:[{name:"show",rawName:"v-show",value:"overview"===t.currentTab,expression:"currentTab === 'overview'"}]},[o("Row",{staticClass:"info-line",staticStyle:{"margin-top":"20px"}},[o("Col",{attrs:{span:"4"}},[t._v("工作流名称：")]),o("Col",{attrs:{span:"8"}},[t._v(t._s(t.workflowInfo.name))]),o("Col",{attrs:{span:"4"}},[t._v("资源URI：")]),o("Col",{attrs:{span:"8"}},[t._v(t._s(t.workflowInfo.uri))])],1),o("Row",{staticClass:"info-line"},[o("Col",{attrs:{span:"4"}},[t._v("最大闲置时间(分)：")]),o("Col",{attrs:{span:"8"}},[t._v(t._s(t.workflowInfo.max_idle_time))]),o("Col",{attrs:{span:"4"}},[t._v("部署状态：")]),o("Col",{attrs:{span:"8"}},[o("i-switch",{model:{value:t.isRunning,callback:function(e){t.isRunning=e},expression:"isRunning"}},[o("span",{attrs:{slot:"open"},slot:"open"},[t._v("是")]),o("span",{attrs:{slot:"close"},slot:"close"},[t._v("否")])])],1)],1),o("Row",{staticClass:"info-line"},[o("Col",{attrs:{span:"12"}},[o("StatsLineChart",{key:1,attrs:{title:"实时请求数",color:"rgba(54, 162, 235, 0.2)",url:"ws://"+t.window.location.host+"/stats/ws/request/"+t.workflowInfo.uri,height:300}})],1)],1)],1),o("Row",{directives:[{name:"show",rawName:"v-show",value:"edit"===t.currentTab,expression:"currentTab === 'edit'"}]},[o("Form",{staticStyle:{"margin-top":"30px"},attrs:{"label-position":"left","label-width":130,rules:t.rulesValidate,model:t.form}},[o("FormItem",{attrs:{label:"工作流名称",prop:"workflowName"}},[o("Row",[o("Col",{attrs:{span:"12"}},[o("Input",{attrs:{value:t.workflowInfo.name,disabled:""}})],1)],1)],1),o("FormItem",{attrs:{label:"URI",prop:"workflowURI"}},[o("Row",[o("Col",{attrs:{span:"20"}},[o("Input",{attrs:{value:t.workflowInfo.uri,disabled:""}})],1)],1)],1),o("FormItem",{attrs:{label:"可选函数列表"}},[o("Row",[o("Col",{attrs:{span:"12"}},[o("input",{staticStyle:{position:"absolute",left:"-999em"},attrs:{id:"dummy-uri"}}),o("ul",{staticStyle:{"list-style":"none","max-height":"100px","overflow-y":"scroll"}},t._l(t.functionList,function(e,s){return o("li",{key:s,staticStyle:{"border-top":"solid 1px lightgrey"},style:s===t.functionLastOne?"border-bottom: solid 1px lightgrey":""},[t._v("\n                "+t._s(e.name)+" (URI: "+t._s(e.uri)+")\n                "),o("Tooltip",{attrs:{content:"copy: "+e.uri,placement:"top"}},[o("Icon",{staticStyle:{color:"blue",cursor:"pointer"},attrs:{size:"16",type:"ios-copy-outline"},on:{click:function(o){return t.copyToClipboard(e.uri)}}})],1)],1)}),0)])],1)],1),o("FormItem",{attrs:{label:"工作流定义(JSON有限状态机)",prop:"definition"}},[o("Row",[o("Col",{attrs:{span:"14"}},[o("AceEditor",{ref:"workflowEditor",staticStyle:{"font-size":"0.9em"},attrs:{lang:"json",theme:"chrome",value:"",width:"100%",height:"430px"},on:{init:t.aceInit},model:{value:t.form.definition,callback:function(e){t.$set(t.form,"definition",e)},expression:"form.definition"}})],1),o("Col",{attrs:{span:"10"}},[o("svg",{staticStyle:{width:"100%",height:"430px"},attrs:{id:"workflow-preview"}},[o("g")])])],1)],1),o("FormItem",{attrs:{label:"最大闲置时间(Minute)",prop:"maxIdleTime"}},[o("Row",[o("Col",{attrs:{span:"6"}},[o("Input",{attrs:{type:"number"},model:{value:t.form.maxIdleTime,callback:function(e){t.$set(t.form,"maxIdleTime",e)},expression:"form.maxIdleTime"}})],1)],1)],1),o("FormItem",[o("Button",{attrs:{type:"primary"}},[t._v("提交")])],1)],1)],1),o("Row",{directives:[{name:"show",rawName:"v-show",value:"test"===t.currentTab,expression:"currentTab === 'test'"}]},[o("Row",[o("Form",{staticStyle:{"margin-top":"30px"},attrs:{"label-position":"left","label-width":130,model:t.testForm}},[o("FormItem",{attrs:{label:"物联网节点IP",prop:"deviceIP"}},[o("Row",[o("Col",{attrs:{span:"8"}},[o("Input",{attrs:{type:"text"},model:{value:t.testForm.deviceIP,callback:function(e){t.$set(t.testForm,"deviceIP",e)},expression:"testForm.deviceIP"}})],1),o("Col",{attrs:{span:"1"}},[t._v(" ")]),o("Col",{attrs:{span:"8"}},[o("Button",{attrs:{type:"primary"},on:{click:t.test}},[t._v("发送")])],1)],1)],1),o("FormItem",{attrs:{label:"输入数据(JSON)",prop:"input"}},[o("Row",[o("Col",{attrs:{span:"24"}},[o("AceEditor",{ref:"inputEditor",staticStyle:{"font-size":"0.9em"},attrs:{lang:"json",theme:"chrome",width:"100%",height:"170px"},model:{value:t.testForm.input,callback:function(e){t.$set(t.testForm,"input",e)},expression:"testForm.input"}})],1)],1)],1),o("FormItem",{attrs:{label:"工作流状态"}},[o("Row",[o("Col",{attrs:{span:"14"}},[o("svg",{staticStyle:{width:"100%",height:"420px"},attrs:{id:"workflow-test"}},[o("g")])]),o("Col",{attrs:{span:"10"}},[o("pre",{staticStyle:{width:"100%",padding:"10px",background:"lightgray","max-height":"420px","overflow-y":"auto","line-height":"1.3"}},[t._v(t._s(t.output)+"\n              ")])])],1)],1)],1)],1),o("Row")],1)],1)},i=[],a=(o("ac6a"),o("456d"),o("5698")),l=o("1c46"),c={name:"WorkflowView",props:["workflowInfo"],components:{AceEditor:o("7c9e")},data:function(){return{currentTab:"overview",testForm:{deviceIP:"",input:""},form:{definition:this.workflowInfo.definition,maxIdleTime:this.workflowInfo.max_idle_time},functionList:[],rulesValidate:{definition:[{type:"string",required:!0}],maxIdleTime:[{type:"number",required:!0}]},workflowUpdater:null,output:"",wsConnection:null}},mounted:function(){var t=this;console.log(this.workflowInfo),this.axios.get("/function").then(function(e){if(200!==e.status)throw new Error(e.status+e.statusText);if("success"!==e.data.status)throw new Error(e.data.info);t.functionList=e.data.data}).catch(function(t){console.error(t)}),o("2099"),o("818b"),o("95b8")},computed:{isRunning:{get:function(){return"running"===this.workflowInfo.status},set:function(){}},functionLastOne:function(){return Object.keys(this.functionList).length-1}},watch:{currentTab:function(t){"edit"===t?setTimeout(this.updatePreview,500):"test"===t&&setTimeout(this.testInitialize,500)},workflowInfo:function(t){this.form.definition=t.definition,this.form.maxIdleTime=t.maxIdleTime}},beforeDestroy:function(){if(null!==this.wsConnection){var t=this.wsConnection.readyState;t!==WebSocket.CLOSED&&t===WebSocket.CLOSING&&this.wsConnection.close()}this.wsConnection=null},methods:{test:function(){var t=this;this.workflowUpdater.clear(),this.axios.post("/test/workflow",{ip:this.testForm.deviceIP,uri:this.workflowInfo.uri,data:this.testForm.input}).then(function(e){if(200!==e.status)throw new Error(e.status+e.statusText);if("success"!==e.data.status)throw new Error(e.data.info);t.output+="".concat(e.data.data,"\n");var o=e.data.data;if(null!==t.wsConnection){var s=t.wsConnection.readyState;s!==WebSocket.CLOSED&&s===WebSocket.CLOSING&&t.wsConnection.close()}t.wsConnection=new WebSocket("ws://".concat(window.location.host,"/test/ws/").concat(o)),t.wsConnection.onmessage=function(e){var o=JSON.parse(e.data);t.workflowUpdater.update(o.role,o.status,o.ip,o.info)},t.wsConnection.onerror=function(t){return console.error(t)},t.wsConnection.onclose=function(){return console.log("ws close")}}).catch(function(e){t.$Message.error(e.message)})},aceInit:function(){var t=this.$refs.workflowEditor.editor;t.on("blur",this.updatePreview)},submit:function(){var t=this;if(null!==this.form.file)this.axios.post("/function/token",{uri:this.workflowInfo.uri}).then(function(e){if(200===e.status){if("success"===e.data.status)return t.axios.put(e.data.data,t.form.file,{headers:{"Content-Type":t.form.file.type}});throw new Error(e.data.info)}throw new Error(e.status+e.statusText)}).then(this.modify).catch(function(e){t.$$Message.error(e.message)});else try{this.modify({status:200})}catch(e){this.$Message.error(e.message)}},modify:function(t){var e=this;if(200!==t.status)throw new Error(t.status+t.statusText);this.axios.post("/function/create",{name:this.form.functionName,uri:this.form.functionURI,memory_limit:this.form.memoryLimit,max_idle_time:this.form.maxIdleTime,environment:this.form.environment,entrypoint:this.form.entrypoint,code_url:this.form.code_url}).then(function(t){if(200!==t.status)throw new Error(t.status+t.statusText);if("success"!==t.data.status)throw new Error(t.data.info);e.$Message.success("创建成功"),e.$router.push("/center/function")})},updatePreview:function(){try{var t=a["c"]("#workflow-preview"),e=t.select("g"),o=new l["c"](t,e),s=new l["a"](JSON.parse(this.form.definition)),n=s.toDAG();o.clear(),o.setNodes(n.nodes),o.setEdges(n.edges),o.setStartNodes(n.startNodes),o.setEndNodes(n.endNodes),o.setParents(n.parents),o.redraw()}catch(r){console.log(r)}},copyToClipboard:function(t){console.log(t);var e=document.querySelector("#dummy-uri");e.value=t,e.select(),document.execCommand("copy")},testInitialize:function(){var t=a["c"]("#workflow-test"),e=t.select("g"),o=new l["c"](t,e),s=new l["a"](JSON.parse(this.workflowInfo.definition)),n=s.toDAG();o.clear(),o.setNodes(n.nodes),o.setEdges(n.edges),o.setStartNodes(n.startNodes),o.setEndNodes(n.endNodes),o.setParents(n.parents),o.redraw(!0),this.workflowUpdater=new l["b"](o,s)}}},u=c,f=(o("320d"),o("2877")),w=Object(f["a"])(u,r,i,!1,null,null,null),d=w.exports,m={name:"WorkflowManage",components:{WorkflowView:d},data:function(){return{workflows:[],current_workflow:null,selected_idx:0}},mounted:function(){var t=this;this.refreshWorkflows(function(){t.selectWorkflow(t.selected_idx)})},methods:{refreshWorkflows:function(t){var e=this;this.axios.get("/workflow").then(function(o){if(200!==o.status)throw new Error(o.status+o.statusText);if("success"!==o.data.status)throw new Error(o.data.info);e.workflows=o.data.data,void 0!==t&&e.$nextTick(t)}).catch(function(t){console.error(t)})},selectWorkflow:function(t){t<0||t>=this.workflows.length||(null!==this.selected_idx&&document.querySelector("#workflow"+this.selected_idx).classList.remove("selected"),document.querySelector("#workflow"+t).classList.add("selected"),this.selected_idx=t,this.current_workflow=this.workflows[t])}}},p=m,h=(o("780c"),Object(f["a"])(p,s,n,!1,null,null,null));e["default"]=h.exports},"320d":function(t,e,o){"use strict";var s=o("e7af"),n=o.n(s);n.a},"780c":function(t,e,o){"use strict";var s=o("b227"),n=o.n(s);n.a},b227:function(t,e,o){},e7af:function(t,e,o){}}]);
//# sourceMappingURL=chunk-50bc560d.2fa9441d.js.map