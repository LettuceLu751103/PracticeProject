<template>
  <p>{{ msg }}</p>
  <p>Author 名字 : {{ names }}</p>
  <div>
    <p v-for="member in members">Team Member: {{ member }}</p>
  </div>
  <div>
    <p>數字相加 {{ number + 10}}</p>
  </div>
  <div>
    <p>狀態變化 {{flag ? '正確' : '錯誤'}}</p>
  </div>
  <div>
    <p>Author 名字反轉 : {{ names.split('').reverse().join('') }}</p>
  </div>
  <p>{{ rawHTML }}</p>
  <p v-html="rawHTML"></p>
</template>

<script>
export default {
  data() {
    return {
      msg: '神奇的VUE框架',
      names: 'Lettuce Lu',
      members: ['Helen', 'Ruby', 'Brian', 'Horace'],
      number: 5,
      flag: false,
      rawHTML: '<a href="https://www.google.com">百戰生菜</a>'
    }
  }
}
</script>