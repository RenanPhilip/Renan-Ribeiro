const addNewTask = document.querySelector('#addNewTask');
const newTaskInput = document.querySelector('#newTask');
const listEl = document.querySelector('#List');

let taskNumer = 0;

function newTask(taskData) {
    const newDiv = document.createElement('div');
    newDiv.className = "task";
    newDiv.draggable = true;

    newDiv.innerHTML = `
        <div class="drag-handle">
            <span></span><span></span><span></span>
        </div>
        <input type="checkbox" class="taskCheckbox">
        <span class="taskText">${taskData}</span>
        <input type="button" class="removeTask" value="Delete">
    `;
    listEl.appendChild(newDiv);
}

function handleAddTask() {
    const task = newTaskInput.value.trim();
    if (task !== '') {
        newTask(task);
    }
    newTaskInput.value = "";
}

addNewTask.addEventListener('click', handleAddTask);

newTaskInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        handleAddTask();
    }
});

listEl.addEventListener('click', (e) => {
    if (e.target && e.target.classList.contains("removeTask")) {
        e.target.parentElement.remove();
    }
});

// Drag & Drop com FLIP Animation
let draggedItem = null;

listEl.addEventListener("dragstart", (e) => {
    if (e.target.classList.contains("task")) {
        draggedItem = e.target;
        e.target.classList.add("dragging");
    }
});

listEl.addEventListener("dragend", (e) => {
    if (e.target.classList.contains("task")) {
        e.target.classList.remove("dragging");
        draggedItem = null;
    }
});

listEl.addEventListener("dragover", (e) => {
    e.preventDefault();
    const afterElement = getDragAfterElement(listEl, e.clientY);

    if (afterElement == null) {
        listEl.appendChild(draggedItem);
    } else {
        if (afterElement !== draggedItem) {
            animateSwap(listEl, draggedItem, afterElement);
            listEl.insertBefore(draggedItem, afterElement);
        }
    }
});

// Função FLIP para animar suavemente os swaps
function animateSwap(container, dragged, target) {
    const children = [...container.querySelectorAll(".task:not(.dragging)")];

    const start = children.map(el => {
        const rect = el.getBoundingClientRect();
        return { el, top: rect.top };
    });

    container.insertBefore(dragged, target);

    const end = children.map(el => {
        const rect = el.getBoundingClientRect();
        return { el, top: rect.top };
    });

    start.forEach((s, i) => {
        const dy = s.top - end[i].top;
        if (dy) {
            requestAnimationFrame(() => {
                s.el.style.transform = `translateY(${dy}px)`;
                s.el.style.transition = "transform 0s";
                requestAnimationFrame(() => {
                    s.el.style.transform = "";
                    s.el.style.transition = "transform 0.25s ease";
                });
            });
        }
    });
}

// Calcula posição para inserir
function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll(".task:not(.dragging)")];

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
