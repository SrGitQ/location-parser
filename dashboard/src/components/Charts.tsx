import React from 'react';
import { MBox } from './boxes';

const Charts: React.FC = () => {
    return (
      <div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
        <MBox>
          Chart 1
        </MBox>
        <MBox>
          Chart 2
        </MBox>
      </div>
    );
};

export default Charts;