import React, { ReactNode } from 'react';

type Props = {
    children: ReactNode;
}

const MBox: React.FC<Props> = (props) => {
    return (
        <div className='h-[29.5rem] bg-neutral-100 rounded-lg p-6'>
            {props.children}
        </div>
    );
};

export default MBox;