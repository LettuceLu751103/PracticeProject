
<template>
    <div class="aside">
        <h3>Aside</h3>
        <Item></Item>
        <Item></Item>
        <Item></Item>
    </div>
</template>

<script>
import Item from './Item.vue'
export default {
    data(){
        return {

        }
    },
    components:{
        Item
    }
}
</script>

<style scoped>
.aside {
    float: right;
    width: 30%;
    height: 600px;
    border: 5px solid #999;
    box-sizing: border-box;

}
</style>