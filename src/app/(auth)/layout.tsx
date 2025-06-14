// src/app/(auth)/layout.tsx
import type { Metadata } from "next";
import "@/app/globals.css";

export const metadata: Metadata = {
  title: "Auth | MyApp",
};

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-tr from-gray-900 via-black to-gray-900 text-white">
      <div className="w-full max-w-md rounded-2xl bg-white/5 p-8 shadow-xl backdrop-blur-md">
        {children}
      </div>
    </div>
  );
}
