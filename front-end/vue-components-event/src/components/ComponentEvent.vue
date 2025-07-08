<template>
    <div class="main-border">
        <h3>Component Event - 組件事件</h3>
        <p>來自子組件的訊息 : <span style="color: red;">{{ messageChild }}</span></p>
        <Child :messageParent="messageParent" @childMessage="getChildMessageHandler"></Child>
    </div>
    
</template>

<script>
import Child from './Child.vue'

export default {
    data(){
            return {
                messageParent: '父組件傳來的數據',
                messageChild: ''
            }
    },
    components:{
        Child
    },
    methods:{
        getChildMessageHandler(data){
            console.log('子組件送資料過來啦!!! ' + data)
            this.messageChild = data
        }
    }
}

</script>

<style>
.main-border {
    border: 3px solid red;
    box-sizing: border-box;
}

</style>