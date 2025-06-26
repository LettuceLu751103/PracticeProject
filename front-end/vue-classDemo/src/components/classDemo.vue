<template>
    <h3>Class 綁定</h3>
    <p :class="classObj">當前字體</p>
    <p>當前字體若是超過上述大小, 則為緊急</p>
    <p>當前字體若是紅色, 則為錯誤</p>
</template>

<script>
    export default {
        data(){
            return {
                classObj:{
                    'isEmergency': true,
                    'isError': true
                },

            }
        }
    }
</script>

<style>
.isEmergency {
    font-size: 26px;
}
.isError {
    color: red;
}
</style>