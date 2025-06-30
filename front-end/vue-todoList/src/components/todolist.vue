<template>
    <h3>todolist 範例</h3>
    <p>清空 todoList <button @click="emptyTodoList()">清空</button></p>
    <p>輸入內容 : {{ inputData }}</p>
    <div>
        <input type="text" v-model="inputData" @input="inputHandler()">
        <button v-on:click="addTodoList()">Add</button>
    </div>
    
    
    <ul>
        <li v-for="(todo, index) in todos" :class="state"><input type="checkbox" @click="ischecked($event, index)" :checked="isChecked" :name="index" :id="index">{{ todo }} <button @click="deleteHandler(index)" :id="index">delete</button></li>
    </ul>
    <div>
        <h5 v-if="todos.length===0">暫無待辦事項</h5>
    </div>
</template>


<script>
    export default {
        data(){
            return {
                inputData:'',
                todos:['Practice Vue Framework', 'Practice Django Framework', 'Practice Ansiblel'],
                isChecked: false,
                state:'',
                
            }
        },
        methods:{
            inputHandler(){
                console.log(this.inputData)
            },
            addTodoList(){
                this.todos.push(this.inputData)
                this.inputData = ''
            },
            deleteHandler(index){
                console.log(`click index : ` + index)
                // splice(index, delete quantity)
                console.log(this.todos.splice(index,1))
            },
            emptyTodoList(){
                this.todos=[]
            },
            ischecked(e){
                console.log(e)
                
            }
        }
    }
</script>

<style>
.delete {
    color: brown;
    text-decoration: line-through;
}
</style>