import type { PropsWithChildren } from "react";

interface IFContainerProps extends PropsWithChildren {
    className?: string;
}

export default function IFContainer({
    children,
    className = "",
}: IFContainerProps) {
    return (
        <div
            className={`
                mx-auto
                w-full
                max-w-screen-2xl

                px-6
                md:px-8
                xl:px-10

                ${className}
            `}
        >
            {children}
        </div>
    );
}