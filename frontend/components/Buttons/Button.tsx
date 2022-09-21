import React, { createContext, useContext } from "react";

type ButtonVariant = "default" | "primary" | "success" | "danger" | "holon__ghost";

type Props = {
  children: React.ReactNode;
  variant?: ButtonVariant;
} & React.ButtonHTMLAttributes<HTMLButtonElement>;

const holonshadow = "shadow-[4px_4px_0_0] border";

const variants: Record<ButtonVariant, string> = {
  default:
    "bg-white text-gray-700 ring-gray-700/10 hover:bg-gray-50 hover:text-gray-900 focus-visible:ring-blue-500 active:bg-gray-100 active:ring-gray-700/20",
  primary:
    "bg-blue-600 text-white ring-blue-500/10 hover:bg-blue-500 hover:text-white focus-visible:ring-blue-700/30 focus-visible:ring-offset-1 active:bg-blue-600 active:ring-blue-500/20",
  success:
    "bg-emerald-600 text-white ring-emerald-500/10 hover:bg-emerald-500 hover:text-white focus-visible:ring-emerald-700/30 focus-visible:ring-offset-1 active:bg-emerald-600 active:ring-emerald-500/20",
  danger:
    "bg-red-600 text-white ring-red-500/10 hover:bg-red-500 hover:text-white focus-visible:ring-red-700/30 focus-visible:ring-offset-1 active:bg-red-600 active:ring-red-500/20",
  holon__ghost: `bg-transparent ${holonshadow}`,
};

const iconVariants: Record<ButtonVariant, string> = {
  danger: "text-red-200",
  default: "text-gray-400",
  holon__ghost: "text-gray-200",
  primary: "text-blue-200",
  success: "text-emerald-200",
};

const ButtonContext = createContext<ButtonVariant | undefined>(undefined);

/**
 * An example Button component with color variants.
 */
export default function Button({ children, variant = "default", ...rest }: Props) {
  const colorClasses = variants[variant] || variants.default;

  return (
    <button
      className={`${colorClasses} relative inline-flex items-center py-2 px-3 font-medium leading-5 shadow-sm outline-none transition focus-visible:ring-2 active:shadow-inner`}
      {...rest}
    >
      <ButtonContext.Provider value={variant}>{children}</ButtonContext.Provider>
    </button>
  );
}

/**
 * Hook which provides access to the button variant.
 */
export function useButtonContext() {
  const context = useContext(ButtonContext);

  if (!context) {
    throw new Error("useButtonContext must be used within a Button");
  }

  return context;
}

interface IconProps {
  children: React.ReactNode;
}

/**
 * Clones the children adding color classes to match the parent button.
 */
Button.Icon = function ButtonIcon({ children }: IconProps) {
  const variant = useButtonContext();
  const variantClasses = iconVariants[variant] || iconVariants.default;

  return (
    <>
      {React.Children.map(children, (child) => {
        if (React.isValidElement(child)) {
          return React.cloneElement(child as React.ReactElement, {
            className: `${child.props.className} mr-2 ${variantClasses}`,
          });
        }

        return null;
      })}
    </>
  );
};
