import React from 'react';
import { LBox } from './boxes';
import { Title } from './text';
const Competency: React.FC = () => {
  return (
		<div className='grid bg-color-red m-6 gap-6'>
      <LBox>
        <Title title='Competency'/>
      </LBox>
		</div>
  );
};

export default Competency;