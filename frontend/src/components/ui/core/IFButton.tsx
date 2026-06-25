import type {
    ButtonHTMLAttributes,
    ReactNode,
} from "react";

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
            border-blue-500/30
            bg-blue-500/10

            hover:bg-blue-500/20
            hover:border-blue-400
            `,

        secondary:
            `
            border-white/10
            bg-white/5

            hover:bg-white/10
            hover:border-white/20
            `,

        ghost:
            `
            border-transparent
            bg-transparent

            hover:bg-white/5
            `,

        danger:
            `
            border-red-500/30
            bg-red-500/10

            hover:bg-red-500/20
            hover:border-red-400
            `,

    };

    return (

        <button

            className={`
                inline-flex
                items-center
                justify-center
                gap-3

                rounded-2xl

                border

                px-10
                py-5

                text-lg
                font-semibold

                text-white

                backdrop-blur-xl

                shadow-lg
                shadow-blue-500/10

                transition-all
                duration-300

                hover:-translate-y-1
                hover:scale-[1.02]
                hover:shadow-2xl
                hover:shadow-blue-500/20

                active:scale-[0.98]

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