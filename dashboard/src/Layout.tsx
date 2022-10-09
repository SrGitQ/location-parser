import React from 'react';
import { BasicInformation, Metrics, Charts, Competency } from './components';

const Layout: React.FC = () => {
    return (
      <div className="grid-rows-4">
        <BasicInformation />
        <Metrics />
        <Charts />
        <Competency />
      </div>
    )
}

export default Layout;