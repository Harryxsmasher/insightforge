import type { HTMLAttributes, PropsWithChildren } from "react";

import { cn } from "../../../lib/cn";

type CardVariant =
    | "glass"
    | "outlined"
    | "solid";

interface IFCardProps
    extends HTMLAttributes<HTMLDivElement>,
        PropsWithChildren {

    variant?: CardVariant;

    hover?: boolean;
}

export default function IFCard({

    variant = "glass",

    hover = true,

    className,

    children,

    ...props

}: IFCardProps) {

    const variants = {

        glass:
            `
            bg-white/[0.04]
            border-white/10
            backdrop-blur-xl
            `,

        outlined:
            `
            bg-transparent
            border-white/10
            `,

        solid:
            `
            bg-[#18181B]
            border-white/10
            `

    };

    return (

        <div

            className={cn(

                `
                rounded-3xl

                border

                p-8

                shadow-xl
                shadow-black/20

                transition-all
                duration-300
                `,

                hover &&
                `
                hover:-translate-y-1
                hover:border-blue-500/20
                hover:shadow-2xl
                `,

                variants[variant],

                className

            )}

            {...props}

        >

            {children}

        </div>

    );

}