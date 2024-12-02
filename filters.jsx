import React from 'react';
import { useDispatch } from 'react-redux';
import { setFilter } from '../redux/taskSlice';

const Filters = () => {
  const dispatch = useDispatch();

  return (
    <div>
      <button onClick={() => dispatch(setFilter('All'))}>All</button>
      <button onClick={() => dispatch(setFilter('Completed'))}>Completed</button>
      <button onClick={() => dispatch(setFilter('Pending'))}>Pending</button>
    </div>
  );
};

export default Filters;
