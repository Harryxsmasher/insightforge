import type { HTMLAttributes, ReactNode } from "react";

type BadgeVariant =
    | "primary"
    | "success"
    | "warning"
    | "danger"
    | "neutral";

interface IFBadgeProps extends HTMLAttributes<HTMLSpanElement> {
    variant?: BadgeVariant;
    children: ReactNode;
}

export default function IFBadge({

    variant = "primary",

    className = "",

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
            border-amber-500/20
            bg-amber-500/10
            text-amber-300
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

            className={`

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

                transition-all
                duration-300

                ${variants[variant]}

                ${className}

            `}

            {...props}

        >

            {children}

        </span>

    );

}