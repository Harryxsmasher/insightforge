import type { PropsWithChildren } from "react";

export default function IFContainer({
    children,
}: PropsWithChildren) {
    return (
        <div
            className="
                mx-auto
                w-full
                max-w-screen-2xl

                px-6

                md:px-8

                xl:px-10
            "
        >
            {children}
        </div>
    );
}