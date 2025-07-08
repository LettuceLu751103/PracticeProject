<template>
    <div class="child-title">
        <h4>Child 組件</h4>
        <p>訊息 : <span style="color: red;">{{ messageParent }}</span></p>
        <div>
            <input type="text" v-model="sendText">
        </div>
        <button @click="clickHandler()">傳遞訊息給父組件</button>
    </div>
</template>

<script>
export default {
    data(){
        return {
            sendText:''
        }
    },
    props:['messageParent'],
    methods:{
        clickHandler(){
            // 自定義事件
            this.$emit('childMessage', this.sendText)
            console.log('點了按鈕 ' + this.sendText)
        }
    }
}
</script>

<style>
.child-title {
    width: 70%;
    border: 5px solid grey;
    height: 200px;
    box-sizing: border-box;
    margin: 0 auto;
}
</style>