
<template>
  <h3>{{ title }}</h3>
  <p v-if="state">你看不看的到我</p>
  <p v-else>前一句看不到, 所以這句看到了</p>
</template>

<script>
export default {
  data(){
    return {
      title:'條件渲染',
      state: true
    }
  }
}
</script>