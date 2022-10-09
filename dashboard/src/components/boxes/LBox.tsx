import React, { ReactNode } from 'react';

type Props = {
    children: ReactNode;
}

const RBox: React.FC<Props> = (props) => {
    return (
        <div className='h-[27rem] bg-zinc-100 rounded-lg p-6'>
            {props.children}
        </div>
    );
}

export default RBox;