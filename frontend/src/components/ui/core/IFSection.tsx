import type { PropsWithChildren } from "react";

interface IFSectionProps
    extends PropsWithChildren {

    className?: string;

}

export default function IFSection({

    children,

    className="",

}: IFSectionProps){

    return(

        <section
            className={`
                py-24

                ${className}
            `}
        >

            {children}

        </section>

    );

}