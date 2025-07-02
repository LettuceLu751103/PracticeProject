<template>
    <h3>Watch Demo</h3>
    <p>Q1. 請選擇下列哪一個答案是監聽器的關鍵字?</p>
    <p @click="clickHandler($event)"> A. methods </p>
    <p @click="clickHandler($event)"> B. data </p>
    <p @click="clickHandler($event)"> C. watch </p>
    <p @click="clickHandler($event)"> D. component </p>
    <p>最終選擇的答案 : {{ answered }}</p>
    <hr>
    <p>最終選擇之前的答案: {{ beforeAnswer }}</p>
    <button @click="changeHandler()">點擊變化數據</button>
</template>


<script>
export default {
    data(){
        return {
            answered : '',
            beforeAnswer: ''
        }
    },
    methods: {
        clickHandler(e){
            console.log(e)
            this.answered = e.target.innerHTML
        }
    },
    watch: {
        answered(newValue, oldValue){
            console.log('舊的數值: ' + oldValue)
            console.log('新的數值: ' + newValue)
            this.beforeAnswer = oldValue
        }
    }
}
</script>