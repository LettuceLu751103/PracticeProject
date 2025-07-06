
<template>
  <Header></Header>
  <Main></Main>
  <Aside></Aside>
</template>

<script>
import Header from './pages/Header.vue'
import Main from './pages/Main.vue'
import Aside from './pages/Aside.vue'

export default {
  // 注入組件
  components:{
    Header,
    Main,
    Aside
  }
}
</script>

<style>
.color {
    color:red;
    font-size: 20px;
}
</style>