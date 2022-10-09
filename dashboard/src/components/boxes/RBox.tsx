import React, { ReactNode } from 'react';

type Props = {
    children: ReactNode;
}

const RBox: React.FC<Props> = (props) => {
    return (
        <div className='h-56 bg-zinc-100 rounded-lg p-6'>
            {props.children}
        </div>
    );
}

export default RBox;