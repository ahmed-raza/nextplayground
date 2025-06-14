// src/app/(auth)/signup/page.tsx
import Link from "next/link";

export default function SignUpPage() {
  return (
    <>
      <h1 className="mb-6 text-3xl font-bold text-center">Sign Up</h1>
      <form className="space-y-4">
        <input
          type="text"
          placeholder="Name"
          className="w-full rounded-md bg-white/10 px-4 py-2 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500"
        />
        <input
          type="email"
          placeholder="Email"
          className="w-full rounded-md bg-white/10 px-4 py-2 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500"
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full rounded-md bg-white/10 px-4 py-2 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500"
        />
        <button
          type="submit"
          className="w-full rounded-md bg-green-600 px-4 py-2 font-semibold hover:bg-green-700"
        >
          Sign Up
        </button>
      </form>
      <p className="mt-4 text-center text-sm text-gray-400">
        Already have an account?{" "}
        <Link href="/signin" className="text-green-400 hover:underline">
          Sign in
        </Link>
      </p>
    </>
  );
}
