import type { ButtonHTMLAttributes, ReactNode } from "react";

type ButtonVariant =
    | "primary"
    | "secondary"
    | "ghost"
    | "danger";

interface IFButtonProps
    extends ButtonHTMLAttributes<HTMLButtonElement> {

    variant?: ButtonVariant;

    fullWidth?: boolean;

    children: ReactNode;
}

export default function IFButton({

    variant = "primary",

    fullWidth = false,

    className = "",

    children,

    ...props

}: IFButtonProps) {

    const variants = {

        primary:
            `
            bg-blue-500/10
            border-blue-500/30
            hover:bg-blue-500/20
            hover:border-blue-400
            `,

        secondary:
            `
            bg-white/5
            border-white/10
            hover:bg-white/10
            hover:border-white/20
            `,

        ghost:
            `
            bg-transparent
            border-transparent
            hover:bg-white/5
            `,

        danger:
            `
            bg-red-500/10
            border-red-500/30
            hover:bg-red-500/20
            hover:border-red-400
            `

    };

    return (

        <button

            className={`

                inline-flex
                items-center
                justify-center
                gap-2

                rounded-2xl

                border

                px-8
                py-4

                font-medium

                text-white

                backdrop-blur-xl

                transition-all
                duration-300

                hover:-translate-y-0.5
                hover:shadow-lg

                active:translate-y-0

                disabled:cursor-not-allowed
                disabled:opacity-50

                ${variants[variant]}

                ${fullWidth ? "w-full" : ""}

                ${className}

            `}

            {...props}

        >

            {children}

        </button>

    );

}