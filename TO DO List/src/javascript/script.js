addNewTask = document.querySelector('#addNewTask')
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

addNewTask.addEventListener('click',()=>{
    task = document.querySelector('#newTask').value
    task != '' ? newTask(task) : console.log(task)
    document.querySelector('#newTask').value = ""
})

removeTask.addEventListener('click',(e)=>{
    e.target.parentElement.remove()
})