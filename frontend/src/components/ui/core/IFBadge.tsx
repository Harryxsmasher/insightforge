import type { PropsWithChildren } from "react";

export default function IFBadge({
    children,
}: PropsWithChildren) {
    return (
        <span
            className="
                inline-flex

                rounded-full

                border
                border-blue-500/20

                bg-blue-500/10

                px-4
                py-2

                text-xs

                uppercase

                tracking-wider

                text-blue-300
            "
        >
            {children}
        </span>
    );
}