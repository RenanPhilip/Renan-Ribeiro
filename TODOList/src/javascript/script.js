addNewTask = document.querySelector('#addNewTask')
newTaskInput = document.querySelector('#newTask')
listEl = document.querySelector('#List')
removeTask = document.querySelector('#removeTask')

taskNumer = 0

newTask = (taskData) => {
    newDiv = document.createElement('div')
    newDiv.id = `task${taskNumer}`   
    newDiv.className = "task"
    newDiv.draggable="true"

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
        e.preventDefault()
        handleAddTask()
    }
})

listEl.addEventListener('click',(e)=>{
    if (e.target && e.target.id.includes("removeTask")){
     e.target.parentElement.remove()
    }
})

// const listEl = document.getElementById('List');
let draggedItem = null;

// Adiciona eventos de drag via handle
function addDragEvents(task) {
    const handle = task.querySelector('.drag-handle');
    handle.addEventListener('mousedown', () => task.setAttribute('draggable', 'true'));
    handle.addEventListener('mouseup', () => task.setAttribute('draggable', 'false'));

    task.addEventListener('dragstart', () => {
        draggedItem = task;
        task.classList.add('dragging');
    });

    task.addEventListener('dragend', () => {
        draggedItem = null;
        task.classList.remove('dragging');
        document.querySelectorAll('.placeholder').forEach(ph => ph.remove());
    });
}

// Inicializa drag em todas as tarefas existentes
document.querySelectorAll('.task').forEach(task => addDragEvents(task));

// Dragover no container da lista
listEl.addEventListener('dragover', e => {
    e.preventDefault();
    const afterElement = getDragAfterElement(listEl, e.clientY);

    document.querySelectorAll('.placeholder').forEach(ph => ph.remove());

    const placeholder = createPlaceholder();
    if (!afterElement) {
        listEl.appendChild(placeholder);
    } else {
        listEl.insertBefore(placeholder, afterElement);
    }
});

// Cria placeholder suave
function createPlaceholder() {
    const placeholder = document.createElement('div');
    placeholder.classList.add('placeholder');
    placeholder.style.height = draggedItem.offsetHeight + 'px';
    return placeholder;
}

// Detecta posição para inserir
function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll('.task:not(.dragging)')];
    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height / 2;
        if (offset < 0 && offset > closest.offset) {
            return { offset: offset, element: child };
        } else {
            return closest;
        }
    }, { offset: Number.NEGATIVE_INFINITY }).element;
}
