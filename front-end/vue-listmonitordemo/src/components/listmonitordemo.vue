<template>

<h3>列表變化監聽</h3>
<ul>
    <li v-for="(item, index) in names" :key="index">{{ item }}</li>
</ul>
<button v-on:click="addListHandler">添加列表數據</button>
</template>

<script>
    export default {
        data(){
            return {
                names:['Brian', 'Ruby', 'Dana', 'Horace', 'Helen']
            }
        },
        methods:{
            addListHandler(){
                this.names = this.names.concat('閃電霹靂車')
                // this.names.push('爆走兄弟')
                // concat, filter, slice 不會被檢測變更方法
                // push, pop, shift, unshift, splice, sort, reverse 會引起變更方法

            }
        }

    }
</script>