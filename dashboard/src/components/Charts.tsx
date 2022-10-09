import React from 'react';
import { MBox } from './boxes';
import { Title } from './text';

const Charts: React.FC = () => {
    return (
      <div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
        <MBox>
          <Title title='Busy days'/>
        </MBox>
        <MBox>
          <Title title='Busy hours'/>
        </MBox>
      </div>
    );
};

export default Charts;