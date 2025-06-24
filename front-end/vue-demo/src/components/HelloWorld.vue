<template>
  <div v-bind:id="dynamicID" v-bind:name="dynamicNAME" v-bind:class="msg">測試</div>
  <button v-bind:disabled="flag">登入按鈕 可用狀態</button>
  <div>
    <button v-bind:disabled="state">登入按鈕 不可用狀態</button>
  </div>
  <div v-bind="attr">
    使用對象的文字, 具有 id, name
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'appClass',
      dynamicID: 'appID',
      dynamicNAME: 'appNAME',
      flag: false,
      state: true,
      attr:{
        class: 'redClass',
        id: 'redId'
      }
    }
  }
}
</script>

<style>
.appClass {
  color: blue;
  font-size: 26px;
}
.redClass {
  color: red;
  font-size: 30px;
}
</style>