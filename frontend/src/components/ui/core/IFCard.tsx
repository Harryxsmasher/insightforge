import type { HTMLAttributes, ReactNode } from "react";

type CardVariant =
    | "default"
    | "outlined"
    | "glass";

interface IFCardProps extends HTMLAttributes<HTMLDivElement> {
    variant?: CardVariant;

    hover?: boolean;

    children: ReactNode;
}

export default function IFCard({

    variant = "glass",

    hover = true,

    className = "",

    children,

    ...props

}: IFCardProps) {

    const variants = {

        default:
            `
            bg-[#18181B]
            border-white/10
            `,

        outlined:
            `
            bg-transparent
            border-white/10
            `,

        glass:
            `
            bg-white/[0.04]
            border-white/10
            backdrop-blur-xl
            `,

    };

    return (

        <div

            className={`

                rounded-3xl

                border

                p-8

                shadow-xl
                shadow-black/20

                transition-all
                duration-300

                ${hover
                    ? `
                        hover:-translate-y-1
                        hover:border-blue-500/20
                        hover:shadow-2xl
                      `
                    : ""
                }

                ${variants[variant]}

                ${className}

            `}

            {...props}

        >

            {children}

        </div>

    );

}