addNewTask = document.querySelector('#addNewTask')
listEl = document.querySelector('#List')
taskNumer = 0

        // <div id="task" class="task">
        //     <input type="checkbox">
        //         Tarefa 02
        //     <input type="button" id="removeTask" value="Delete">
        // </div>

newTask = (taskData) => {
    newDiv = document.createElement('div')
    newDiv.id = `task${taskNumer}`   
    newDiv.className = "task"

    newDiv.innerHTML = `<input type="checkbox">
    ${taskData}
    <input type="button" id="removeTask" value="Delete">`
    listEl.appendChild(newDiv)

    taskNumer++
}
addNewTask.addEventListener('click',()=>{
    task = document.querySelector('#newTask').value
    task != '' ? newTask(task) : console.log(task)
    document.querySelector('#newTask').value = ""
})