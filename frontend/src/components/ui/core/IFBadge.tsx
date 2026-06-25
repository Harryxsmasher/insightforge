import type {
    HTMLAttributes,
    PropsWithChildren,
} from "react";

import { cn } from "../../../lib/cn";

type BadgeVariant =
    | "primary"
    | "success"
    | "warning"
    | "danger"
    | "neutral";

interface IFBadgeProps
    extends HTMLAttributes<HTMLSpanElement>,
        PropsWithChildren {

    variant?: BadgeVariant;
}

export default function IFBadge({

    variant = "primary",

    className,

    children,

    ...props

}: IFBadgeProps) {

    const variants = {

        primary:
            `
            border-blue-500/20
            bg-blue-500/10
            text-blue-300
            `,

        success:
            `
            border-emerald-500/20
            bg-emerald-500/10
            text-emerald-300
            `,

        warning:
            `
            border-yellow-500/20
            bg-yellow-500/10
            text-yellow-300
            `,

        danger:
            `
            border-red-500/20
            bg-red-500/10
            text-red-300
            `,

        neutral:
            `
            border-white/10
            bg-white/5
            text-slate-300
            `

    };

    return (

        <span

            className={cn(

                `
                inline-flex

                items-center
                justify-center

                rounded-full

                border

                px-4
                py-2

                text-xs
                font-medium

                uppercase
                tracking-wider
                `,

                variants[variant],

                className

            )}

            {...props}

        >

            {children}

        </span>

    );

}