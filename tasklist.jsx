import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { deleteTask, markTaskComplete } from '../redux/taskSlice';

const TaskList = () => {
  const tasks = useSelector((state) => state.tasks.tasks);
  const filter = useSelector((state) => state.tasks.filter);
  const dispatch = useDispatch();

  const filteredTasks = tasks.filter((task) => {
    if (filter === 'Completed') return task.completed;
    if (filter === 'Pending') return !task.completed;
    return true;
  });

  return (
    <div>
      {filteredTasks.map((task) => (
        <div key={task.id}>
          <h4>{task.title}</h4>
          <p>{task.description}</p>
          <button onClick={() => dispatch(markTaskComplete(task.id))}>Complete</button>
          <button onClick={() => dispatch(deleteTask(task.id))}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default TaskList;
