<template>
  <SlotBase>
    <div>
      <h3>插槽標題</h3>
      <p>插槽內容</p>
    </div>
  </SlotBase>
</template>

<script>
import SlotBase from './components/SlotBase.vue'
export default {
  data(){

  },
  components:{
    SlotBase
  }
}
</script>