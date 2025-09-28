addNewTask = document.querySelector('#addNewTask')
newTaskInput = document.querySelector('#newTask')
listEl = document.querySelector('#List')
removeTask = document.querySelector('#removeTask')

taskNumer = 0

newTask = (taskData) => {
    newDiv = document.createElement('div')
    newDiv.id = `task${taskNumer}`   
    newDiv.className = "task"

    newDiv.innerHTML = `<input type="checkbox" id="checkbox">
    ${taskData}
    <input type="button" id="removeTask" value="Delete">`
    listEl.appendChild(newDiv)

    taskNumer++
}

handleAddTask = () => {
    task = document.querySelector('#newTask').value.trim()
    task != '' ? newTask(task) : console.log(task)
    document.querySelector('#newTask').value = ""
}

addNewTask.addEventListener('click', handleAddTask)

newTaskInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault() // evita submit de formulário
        handleAddTask()
    }
})

listEl.addEventListener('click',(e)=>{
    if (e.target && e.target.id.includes("removeTask")){
     e.target.parentElement.remove()
    }
})