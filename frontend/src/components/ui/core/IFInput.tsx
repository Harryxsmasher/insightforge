import type { InputHTMLAttributes } from "react";

import { cn } from "../../../lib/cn";

interface IFInputProps
    extends InputHTMLAttributes<HTMLInputElement> {}

export default function IFInput({

    className,

    ...props

}: IFInputProps) {

    return (

        <input

            className={cn(

                `
                w-full

                rounded-2xl

                border
                border-white/10

                bg-white/5

                px-5
                py-4

                text-white

                placeholder:text-slate-500

                outline-none

                transition-all
                duration-300

                focus:border-blue-500
                focus:ring-2
                focus:ring-blue-500/20
                `,

                className

            )}

            {...props}

        />

    );

}