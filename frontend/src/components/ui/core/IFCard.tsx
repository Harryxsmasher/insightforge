import type { PropsWithChildren } from "react";

export default function IFCard({
    children,
}: PropsWithChildren) {
    return (
        <div
            className="
                rounded-3xl

                border
                border-white/10

                bg-white/5

                backdrop-blur-xl

                shadow-xl

                p-8

                transition-all
                duration-300

                hover:border-blue-500/20
                hover:bg-white/[0.06]
            "
        >
            {children}
        </div>
    );
}