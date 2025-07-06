<template>
    <h3>Search Demo - 模糊搜索</h3>
    <input type="text" v-model.trim="searchData"> 
    <p>Search's String => {{ searchData }}</p>
    <ul>
        <template v-for="(item, index) in datalists" :key="index">
            <div v-if="item.includes(searchData)">
                {{ item }}
            </div>
        </template>
    </ul>
</template>


<script>
    export default {
        data(){
            return {
                datalists:['aaa', 'abb', 'aab', 'bcc', 'abc', 'bcd', 'add', 'acd'],
                searchData: ''
            }
        }
    }
</script>