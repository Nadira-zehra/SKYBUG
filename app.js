import React from 'react';
import TaskList from './components/TaskList';
import Filters from './components/Filters';

const App = () => {
  return (
    <div>
      <h1>Task Management Dashboard</h1>
      <Filters />
      <TaskList />
    </div>
  );
};

export default App;
