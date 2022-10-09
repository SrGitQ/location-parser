import React from 'react';

type Props = {
    children: React.ReactNode;
}

const Bullet: React.FC<Props> = (props) => {
    return (
        <div className='text-neutral-400 text-lg'>
            {props.children}
        </div>
    );
}

export default Bullet;